# ZDI-25-934: MindManager Attachment Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-934
- **ZDI-CAN:** ZDI-CAN-26144
- **Date:** 2025-10-07
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** MindManager
- **Affected Products:** MindManager
- **Credit:** AspiringYoungMan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-934/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MindManager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of attachments. When opening an attachment, the user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to execute code in the context of current user.

## Additional Details

Fixed in version 25.0.208

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-10-07 - Coordinated public release of advisory
- 2025-10-07 - Advisory Updated
