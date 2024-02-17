<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar';

	let bookmarks = false;
	let fullUrls = true;

	const profileRadioValue = 'benoit';
</script>

<div class="m-fit p-4">
	<Menubar.Root class="w-fit">
		<Menubar.Menu>
			<Menubar.Trigger>Data</Menubar.Trigger>
			<Menubar.Content>
				<Menubar.Item href="/processing/file/upload">Upload data file</Menubar.Item>
				<Menubar.Item href="/processing/file/download">Download data file</Menubar.Item>
				<Menubar.Separator />
				<Menubar.Item>
					Print... <Menubar.Shortcut>P</Menubar.Shortcut>
				</Menubar.Item>
			</Menubar.Content>
		</Menubar.Menu>
		<Menubar.Menu>
			<Menubar.Trigger>Pre-processing</Menubar.Trigger>
			<Menubar.Content>
				<Menubar.Sub>
					<Menubar.SubTrigger>Missing Values</Menubar.SubTrigger>
					<Menubar.SubContent>
						<Menubar.Item>Description</Menubar.Item>
						<Menubar.Item>Remove</Menubar.Item>
						<Menubar.Item>Replace with mean</Menubar.Item>
						<Menubar.Item>Replace with median</Menubar.Item>
						<Menubar.Item>Replace with mode</Menubar.Item>
					</Menubar.SubContent>
				</Menubar.Sub>
				<Menubar.Sub>
					<Menubar.SubTrigger>Duplicate rows</Menubar.SubTrigger>
					<Menubar.SubContent>
						<Menubar.Item>Description</Menubar.Item>
						<Menubar.Item>Remove</Menubar.Item>
					</Menubar.SubContent>
				</Menubar.Sub>
				<Menubar.Sub>
					<Menubar.SubTrigger>Constant features</Menubar.SubTrigger>
					<Menubar.SubContent>
						<Menubar.Item>Description</Menubar.Item>
						<Menubar.Item>Remove</Menubar.Item>
					</Menubar.SubContent>
				</Menubar.Sub>
				<Menubar.Sub>
					<Menubar.SubTrigger>Outliers</Menubar.SubTrigger>
					<Menubar.SubContent>
						<Menubar.Item>Description</Menubar.Item>
						<Menubar.Item>Drop based on z-score</Menubar.Item>
						<Menubar.Item>Drop based on IQR</Menubar.Item>
					</Menubar.SubContent>
				</Menubar.Sub>
				<Menubar.Item>Remove columns</Menubar.Item>
				<Menubar.Item>Label encoding</Menubar.Item>
			</Menubar.Content>
		</Menubar.Menu>
		<Menubar.Menu>
			<Menubar.Trigger>View</Menubar.Trigger>
			<Menubar.Content>
				<Menubar.CheckboxItem bind:checked={bookmarks}
					>Always Show Bookmarks Bar</Menubar.CheckboxItem
				>
				<Menubar.CheckboxItem bind:checked={fullUrls}>Always Show Full URLs</Menubar.CheckboxItem>
				<Menubar.Separator />
				<Menubar.Item inset>
					Reload <Menubar.Shortcut>R</Menubar.Shortcut>
				</Menubar.Item>
				<Menubar.Item inset>
					Force Reload <Menubar.Shortcut>⇧R</Menubar.Shortcut>
				</Menubar.Item>
				<Menubar.Separator />
				<Menubar.Item inset>Toggle Fullscreen</Menubar.Item>
				<Menubar.Separator />
				<Menubar.Item inset>Hide Sidebar</Menubar.Item>
			</Menubar.Content>
		</Menubar.Menu>
		<Menubar.Menu>
			<Menubar.Trigger>Profiles</Menubar.Trigger>
			<Menubar.Content>
				<Menubar.RadioGroup value={profileRadioValue}>
					<Menubar.RadioItem value="andy">Andy</Menubar.RadioItem>
					<Menubar.RadioItem value="benoit">Benoit</Menubar.RadioItem>
					<Menubar.RadioItem value="Luis">Luis</Menubar.RadioItem>
				</Menubar.RadioGroup>
				<Menubar.Separator />
				<Menubar.Item inset>Edit...</Menubar.Item>
				<Menubar.Separator />
				<Menubar.Item inset>Add Profile...</Menubar.Item>
			</Menubar.Content>
		</Menubar.Menu>
	</Menubar.Root>
</div>
