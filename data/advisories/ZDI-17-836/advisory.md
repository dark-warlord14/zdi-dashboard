# ZDI-17-836: Hewlett Packard Enterprise Intelligent Management Center dbman Opcode 10012 Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-836
- **ZDI-CAN:** ZDI-CAN-4896
- **Date:** 2017-10-03
- **CVE:** CVE-2017-12561
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-836/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within dbman service, which listens on TCP port 2810 by default. A crafted opcode 10012 message can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03781en_us

## Disclosure Timeline

- 2017-06-27 - Vulnerability reported to vendor
- 2017-10-03 - Coordinated public release of advisory
