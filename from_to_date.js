function fillDateInputs(startDate, endDate) {
    const formatOptions = { year: 'numeric', month: '2-digit', day: '2-digit' };
    
    document.getElementById('PickReleaseDateFrom').value = startDate.toLocaleDateString(undefined, formatOptions);
    document.getElementById('PickReleaseDateTo').value = endDate.toLocaleDateString(undefined, formatOptions);
    document.getElementById('NotaIssueDateFrom').value = new Date(startDate.getFullYear(), startDate.getMonth(), 1).toLocaleDateString(undefined, formatOptions);
    document.getElementById('NotaIssueDateTo').value = endDate.toLocaleDateString(undefined, formatOptions);
  }
  
  const currentDate = new Date();
  const startDate = new Date(currentDate);
  startDate.setMonth(currentDate.getMonth() - 1);
  startDate.setDate(1);
  
  fillDateInputs(startDate, currentDate);
  