<script>


function printMessage() {
  console.log("Mensaje impreso desde el trabajador");
  setTimeout(printMessage, 0.5);
}


self.addEventListener('message', function(e) {
  const message = e.data;
  if (message === 'Comenzar') {
    printMessage();
  }
});
</script>
