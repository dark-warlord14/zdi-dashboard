# ZDI-17-481: Hewlett Packard Enterprise Intelligent Management Center dbman Opcode 10005 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-481
- **ZDI-CAN:** ZDI-CAN-4380
- **Date:** 2017-08-07
- **CVE:** CVE-2017-8957
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-481/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within dbman service, which listens by default on TCP port 2810. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: http://h20565.www2.hpe.com/hpsc/doc/public/display?docId=hpesbhf03764en_us

## Disclosure Timeline

- 2017-01-10 - Vulnerability reported to vendor
- 2017-08-07 - Coordinated public release of advisory
