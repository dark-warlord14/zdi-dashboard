# ZDI-20-269: Cisco WebEx Network Recording Player ARF File Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-269
- **ZDI-CAN:** ZDI-CAN-9491
- **Date:** 2020-03-05
- **CVE:** CVE-2020-3127
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-269/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ARF files. Crafted data in an ARF file can trigger access to memory prior to initialization. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200304-webex-player

## Disclosure Timeline

- 2019-10-24 - Vulnerability reported to vendor
- 2020-03-05 - Coordinated public release of advisory
