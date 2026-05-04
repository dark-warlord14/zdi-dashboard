# ZDI-16-617: Dell SonicWALL Universal Management Suite ImagePreviewServlet SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-617
- **ZDI-CAN:** ZDI-CAN-3748
- **Date:** 2016-12-02
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Dell
- **Affected Products:** SonicWALL Universal Management Suite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-617/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dell SonicWALL Universal Management Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ImagePreviewServlet servlet. A SQL Injection vulnerability exists in processing of the logoID parameter. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Dell has issued an update to correct this vulnerability. More details can be found at: https://support.sonicwall.com/product-notification/215257?productName=SonicWALL%20GMS

## Disclosure Timeline

- 2016-05-09 - Vulnerability reported to vendor
- 2016-12-02 - Coordinated public release of advisory
