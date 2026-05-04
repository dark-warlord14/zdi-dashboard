# ZDI-23-455: Ivanti Avalanche getLogFile Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-455
- **ZDI-CAN:** ZDI-CAN-17769
- **Date:** 2023-04-24
- **CVE:** CVE-2023-28127
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-455/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary files on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the getLogFile function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/New-Avalanche-Landing-Page?language=en_US

## Disclosure Timeline

- 2022-07-07 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
