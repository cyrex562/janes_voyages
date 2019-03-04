$(document).ready(function () {
    console.log("ready");
    //
    $("#refresh_voyage_table").click(function (evt) {
        evt.preventDefault();
        window.location.reload();
    });

    // inline voyage form create
    $("#create_voyage_inline").click(function (evt) {
        evt.preventDefault();

        let ship = $("#voyage_ship").val();
        let captain = $("#voyage_captain").val();
        let sources = $("#voyage_sources").val();
        let description = $("#voyage_description").val();

        let req = {
            "ship": ship,
            "ship_captain": captain,
            "sources": sources,
            "description": description
        };
        let req_str = JSON.stringify((req));
        console.log("req: " + req_str);

        let posted = $.post({
            url: "/api/voyages/",
            data: req_str,
            dataType: "json"
        });
        posted.done(function () {
            console.log("reloading voyage list window");
            window.location.reload();
        });
    });

    // detail voyage button
    $("button.voyage_detail_btn").click(function (evt) {
        let voyage_id = this.attributes.action_id.val();
        // $.get("/voyages/" + voyage_id + "/detail/");
        window.location.href("/voyages/" + voyage_id + "/")
    });

    // delete voyage button
    $("button.voyage_delete_btn").click(function (evt) {
        let voyage_id = this.attributes.action_id.val();
        let delete_req = $.ajax({
            url: "/voyages/" + voyage_id, type: "DELETE", success: function (result) {
                console.log("reloading voyage list window");
                window.location.reload();
            }
        });

    })
});