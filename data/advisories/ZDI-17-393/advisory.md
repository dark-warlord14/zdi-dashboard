# ZDI-17-393: Hewlett Packard Enterprise Universal CMDB UploadFileOnUIServerServlet Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-393
- **ZDI-CAN:** ZDI-CAN-4342
- **Date:** 2017-06-12
- **CVE:** CVE-2017-8947
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Universal CMDB
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-393/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Universal CMDB. Authentication is not required to exploit this vulnerability. The specific flaw exists within UploadFileOnUIServerServlet servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbgn03758en_us

## Disclosure Timeline

- 2016-12-15 - Vulnerability reported to vendor
- 2017-06-12 - Coordinated public release of advisory
