# ZDI-18-140: Hewlett Packard Enterprise Intelligent Management Center dbman Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-140
- **ZDI-CAN:** ZDI-CAN-5120
- **Date:** 2018-01-25
- **CVE:** CVE-2017-8981
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-140/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within dbman.exe. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03813en_us

## Disclosure Timeline

- 2017-09-20 - Vulnerability reported to vendor
- 2018-01-25 - Coordinated public release of advisory
- 2018-01-25 - Advisory Updated
