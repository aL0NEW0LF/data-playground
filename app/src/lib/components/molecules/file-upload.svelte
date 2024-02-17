<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import * as Form from '$lib/components/ui/form';
	import { Label } from '../ui/label';
	import { Button } from '../ui/button';
	import { globalData } from '$stores/global-data';

	async function loadData(event: Event) {
		const formElement = event.target as HTMLFormElement;

		const formData = new FormData(formElement);

		const response = await fetch(formElement.action, {
			method: 'POST',
			body: formData
		});

		const responseData = await response.json();
		globalData.set(responseData);
	}
</script>

<form
	method="post"
	action="http://127.0.0.1:5000/process/file/tojson"
	enctype="multipart/form-data"
	on:submit|preventDefault={loadData}
	class="flex flex-col gap-4"
>
	<Label>File</Label>
	<Input class="w-96" id="datafile" name="datafile" type="file" />
	<Button class="" variant="outline" type="submit">Upload</Button>
</form>
