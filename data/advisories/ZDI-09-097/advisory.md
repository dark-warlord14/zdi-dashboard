# ZDI-09-097: Hewlett-Packard OpenView NNM nnmRptConfig.exe Template Variable strcat Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-097
- **ZDI-CAN:** ZDI-CAN-523
- **Date:** 2009-12-09
- **CVE:** CVE-2009-3849
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-097/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard OpenView Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the nnmRptConfig.exe CGI executable accessible via the IIS web server listening by default on TCP port 80. While parsing POST variables this process copies the contents of the Template parameter into a fixed length stack buffer using a strcat call. By supplying a large enough value this buffer can be overflowed leading to arbitrary code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01950877

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2009-12-09 - Coordinated public release of advisory
