# ZDI-17-192: Hewlett Packard Enterprise Intelligent Management Center Service Operation Manager Module FileDownloadServlet filePath Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-192
- **ZDI-CAN:** ZDI-CAN-4057
- **Date:** 2017-03-29
- **CVE:** CVE-2017-5797
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-192/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within Service Operation Manager Module's FileDownloadServlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: http://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03719en_us

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-03-29 - Coordinated public release of advisory
