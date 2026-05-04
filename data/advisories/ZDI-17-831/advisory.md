# ZDI-17-831: Hewlett Packard Enterprise Intelligent Management Center MibBrowserTopoFilterServlet Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-831
- **ZDI-CAN:** ZDI-CAN-4759
- **Date:** 2017-10-03
- **CVE:** CVE-2017-12556
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-831/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MibBrowserTopoFilterServlet, which listens on TCP ports 8080 and 8443 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03778en_us

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-10-03 - Coordinated public release of advisory
