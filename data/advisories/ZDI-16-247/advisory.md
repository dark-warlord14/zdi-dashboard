# ZDI-16-247: Hewlett Packard Enterprise Data Protector EXEC_SCRIPT Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-247
- **ZDI-CAN:** ZDI-CAN-3354
- **Date:** 2016-04-27
- **CVE:** CVE-2016-2007
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Data Protector
- **Credit:** IntR0Py
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-247/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within OmniInet.exe which listens by default on TCP port 5555. When parsing a malformed EXEC_SCRIPT request, the process blindly copies user supplied data into a fixed-length stack buffer. A remote attacker can abuse this to execute remote code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hpe.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c05085988

## Disclosure Timeline

- 2015-12-22 - Vulnerability reported to vendor
- 2016-04-27 - Coordinated public release of advisory
