# ZDI-17-343: Hewlett Packard Enterprise Intelligent Management Center dbman Opcode 10007 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-343
- **ZDI-CAN:** ZDI-CAN-4387
- **Date:** 2017-05-15
- **CVE:** CVE-2017-5819
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-343/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dbman service, which listens on TCP port 2810 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03745en_us

## Disclosure Timeline

- 2017-01-03 - Vulnerability reported to vendor
- 2017-05-15 - Coordinated public release of advisory
