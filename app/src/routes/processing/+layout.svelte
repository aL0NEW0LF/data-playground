<script>
	import Toolsbar from '$lib/components/organisms/toolsbar.svelte';
</script>

<div class="w-full">
	<Toolsbar />
	<div class="mx-4 min-h-screen">
		<slot />
	</div>
</div>
