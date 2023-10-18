const formatOptions = { year: 'numeric', month: '2-digit', day: '2-digit' };
const currentDate = new Date();
const startDate = new Date(currentDate);
startDate.setMonth(currentDate.getMonth() - 1);
startDate.setDate(1);

document.getElementById('PickReleaseDateFrom').value = startDate.toLocaleDateString(undefined, formatOptions);
document.getElementById('PickReleaseDateTo').value = currentDate.toLocaleDateString(undefined, formatOptions);
document.getElementById('NotaIssueDateFrom').value = new Date(startDate.getFullYear(), startDate.getMonth(), 1).toLocaleDateString(undefined, formatOptions);
document.getElementById('NotaIssueDateTo').value = currentDate.toLocaleDateString(undefined, formatOptions);
