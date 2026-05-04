# ZDI-25-040: Ivanti Endpoint Manager DecodeBase64Object Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-040
- **ZDI-CAN:** ZDI-CAN-25432
- **Date:** 2025-01-19
- **CVE:** CVE-2024-13163
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. Alternatively, no user interaction is required if the attacker has administrative credentials to the application. The specific flaw exists within the implementation of the DecodeBase64Object method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-January-2025-for-EPM-2024-and-EPM-2022-SU6

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-01-19 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated
