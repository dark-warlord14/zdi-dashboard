# ZDI-25-148: (0Day) Microsoft Windows LNK File UI Misrepresentation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-148
- **ZDI-CAN:** ZDI-CAN-25373
- **Date:** 2025-03-18
- **CVE:** CVE-2025-9491
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-148/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of .LNK files. Crafted data in an .LNK file can cause hazardous content in the file to be invisible to a user who inspects the file via the Windows-provided user interface. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

09/20/24 – ZDI reported the vulnerability to the vendor. 09/23/24 – The vendor acknowledged the report. 09/27/24 – The vendor assessed the case as not meeting the bar servicing. 11/08/24 – ZDI followed up and provided more information about the case. 11/11/24 – The vendor informed us that they would review the information provided. 03/03/25 – After multiple exchanges, the vendor decided their assessment would remain unchanged. 07/30/25 - ZDI informed the vendor that the case will be published as a zero-day advisory. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2024-09-20 - Vulnerability reported to vendor
- 2025-03-18 - Coordinated public release of advisory
- 2025-10-30 - Advisory Updated
