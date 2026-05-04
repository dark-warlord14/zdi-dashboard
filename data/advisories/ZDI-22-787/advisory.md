# ZDI-22-787: Ivanti Avalanche AgentTaskHandler Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-787
- **ZDI-CAN:** ZDI-CAN-15967
- **Date:** 2022-05-26
- **CVE:** CVE-2022-36982
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-787/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary files on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the AgentTaskHandler class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored session cookies, leading to further compromise.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.3.4_release_notes.txt

## Disclosure Timeline

- 2021-12-08 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
- 2022-07-27 - Advisory Updated
