# ZDI-17-835: Hewlett Packard Enterprise Intelligent Management Center mibFileServlet Directory Traversal Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-835
- **ZDI-CAN:** ZDI-CAN-4809
- **Date:** 2017-10-03
- **CVE:** CVE-2017-12560
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:N/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-835/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary directories on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within mibFileServlet servlet, which listens on TCP ports 8080 and 8443 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete any directories accessible to SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03777en_us

## Disclosure Timeline

- 2017-05-11 - Vulnerability reported to vendor
- 2017-10-03 - Coordinated public release of advisory
