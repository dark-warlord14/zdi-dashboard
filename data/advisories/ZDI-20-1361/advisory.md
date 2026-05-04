# ZDI-20-1361: Cisco WebEx Network Recording Player ARF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1361
- **ZDI-CAN:** ZDI-CAN-11133
- **Date:** 2020-11-10
- **CVE:** CVE-2020-3603
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1361/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ARF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-webex-nbr-NOS6FQ24

## Disclosure Timeline

- 2020-06-05 - Vulnerability reported to vendor
- 2020-11-10 - Coordinated public release of advisory
