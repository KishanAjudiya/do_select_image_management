 var previous_image_name = "";

    function readURL(input, target_id) {
        console.log(target_id);
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $('#' + target_id).attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    };


    function delete_image(input) {
        var data = {
            "image_name": input.id
        }
        console.log(data);
        var request = $.ajax({
            url: "/manage-image/",
            method: "DELETE",
            data: data
        });

        request.done(function(msg) {
            alert(msg['msg']);
            location.reload();
        });

        request.fail(function(jqXHR, textStatus) {
            alert("Request failed: " + textStatus);
        });
    };

    function update_image(input) {
        openAttachment();
        previous_image_name = input.name.replace(/[&\/\\#,+()$~%.'":*?<>{}]/g, '');

    };

    $("#update_file").change(function() {
        readURL(this, "img_" + previous_image_name);
    });

    $("#image_data").change(function() {
        readURL(this, "b64_image_data");
    });


    $('#upload').click(function() {
        var data = {
            "image_name": $('#image_data').val().split('\\').pop(),
            "image_data": $('#b64_image_data').attr('src')
        }
        var request = $.ajax({
            url: "/manage-image/",
            method: "POST",
            data: data
        });

        request.done(function(msg) {
            alert(msg['msg']);
            location.reload();
        });

        request.fail(function(jqXHR, textStatus) {
            alert("Request failed: " + textStatus);
        });
    });

    function openAttachment() {
        var click_on_button = document.getElementById('update_file').click();

    }
    function save_updated_image(input){
    var data = {
            "image_name": input.name,
            "image_data": $('#img' + input.name.replace(/[&\/\\#,+()$~%.'":*?<>{}]/g, '')).attr('src')
        }
        var request = $.ajax({
            url: "/manage-image/",
            method: "PUT",
            data: data
        });

        request.done(function(msg) {
            alert(msg['msg']);
            location.reload();
        });

        request.fail(function(jqXHR, textStatus) {
            alert("Request failed: " + textStatus);
        });}
    $(function() {
        var request = $.ajax({
            url: "/get-all-images",
            method: "GET"
        });

        request.done(function(data) {
            if (Object.keys(data).length) {
                for (var i = 0; i < Object.keys(data).length; i++) {
                    var image_name = Object.keys(data)[i];
                    var image_data = Object.values(data)[i];
                    if (image_name && image_data) {
                        $('#image_list').prepend('<img type="image" name=' + image_name + ' id=img_' + image_name.replace(/[&\/\\#,+()$~%.'":*?<>{}]/g, '') + ' src="' + image_data + '" style="height:100px; width: 100px"/> <input type = "button"value = "Change" name="' + image_name + '" onclick = "update_image(this)"/ ><input type='button' value='save' name=' + image_name +' onclick="save_updated_image(this);"> <input onclick = "delete_image(this);" value = "delete" type = "button" id = "' +
                        image_name + '" ><br>
                        <br> ')
                    }
                }
            };
        });

        request.fail(function(jqXHR, textStatus) {
            alert(jqXHR.responseJSON['msg']);
        });
    });