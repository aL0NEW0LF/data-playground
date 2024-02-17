<script lang="ts">
	import FileUpload from '$lib/components/molecules/file-upload.svelte';
	import * as Table from '$lib/components/ui/table';
	import { globalData } from '$stores/global-data';

	let localData: any[];
	let dataHeaders: string[];

	const unsubscribe = globalData.subscribe((value) => {
		localData = value;
		dataHeaders = [];
		console.log(localData);

		for (let key in localData[0]) {
			dataHeaders.push(key);
		}

		console.log(dataHeaders);
	});
</script>

<div class="flex flex-row gap-4 justify-center">
	<FileUpload />

	<Table.Root class="mt-7">
		<Table.Header>
			<Table.Row>
				{#each dataHeaders as header}
					<Table.Head class="h-10">{header}</Table.Head>
				{/each}
			</Table.Row>
		</Table.Header>
		{#each localData as dataRow, index (index)}
			<Table.Row class="w-min">
				{#each Object.keys(dataRow) as key}
					<Table.Cell class="w-min">{dataRow[key]}</Table.Cell>
				{/each}
			</Table.Row>
		{/each}
		<Table.Caption>A list of your data.</Table.Caption>
		<Table.Body></Table.Body>
	</Table.Root>
</div>
