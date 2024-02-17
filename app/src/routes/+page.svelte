<script>
	import { Button } from '$lib/components/ui/button';
	import Header from '$lib/components/organisms/header.svelte';
</script>

<svelte:head>
	<title>Data Playground</title>
	<meta name="description" content="Data Playground" />
</svelte:head>

<Header />
<section class="my-72">
	<div class="flex flex-row gap-8 items-center justify-center">
		<div class="flex flex-col gap-8 items-center justify-center w-6/12">
			<div class="w-full text-justify">
				Unlock the full potential of your data with our all-in-one web app! Whether you're a data
				enthusiast, analyst, or a machine learning enthusiast, our platform empowers you to
				seamlessly upload, visualize, process, and train machine learning models on your data.
			</div>
			<Button class="" variant="outline" href="processing/file/upload">Get started</Button>
		</div>
	</div>
</section>
