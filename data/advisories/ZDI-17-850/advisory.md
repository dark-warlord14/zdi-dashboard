# ZDI-17-850: Hewlett Packard Enterprise Intelligent Management Center TopoMsgServlet Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-850
- **ZDI-CAN:** ZDI-CAN-4815
- **Date:** 2017-11-06
- **CVE:** CVE-2017-8966
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-850/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within TopoMsgServlet servlet, which listens on TCP ports 8080 and 8443 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03787en_us

## Disclosure Timeline

- 2017-05-11 - Vulnerability reported to vendor
- 2017-11-06 - Coordinated public release of advisory
