# ZDI-19-160: Cisco WebEx Network Recording Player ARF File Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-160
- **ZDI-CAN:** ZDI-CAN-7045
- **Date:** 2019-01-29
- **CVE:** CVE-2019-1639
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-160/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ARF files. Crafted data in an ARF file can trigger a write past the end of an allocated buffer. An attacker may be able to leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20190123-webex-rce

## Disclosure Timeline

- 2018-08-03 - Vulnerability reported to vendor
- 2019-01-29 - Coordinated public release of advisory
