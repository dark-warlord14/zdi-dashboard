# ZDI-25-102: (0Day) Delta Electronics ISPSoft DVP File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-102
- **ZDI-CAN:** ZDI-CAN-25225
- **Date:** 2025-03-03
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** ISPSoft
- **Credit:** Guillaume Orlando
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics ISPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DVP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

09/10/24 – ZDI reported the vulnerability to the ICS-CERT 09/12/24 – ICS-CERT acknowledged the receipt of the report 11/21/24 – the vendor communicated that the fix would be released by the end of January 2025 01/13/25 - ZDI asked for updates 01/22/25 – the vendor requested an extension until the end of April 2025 13/02/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-09-10 - Vulnerability reported to vendor
- 2025-03-03 - Coordinated public release of advisory
- 2025-03-03 - Advisory Updated
