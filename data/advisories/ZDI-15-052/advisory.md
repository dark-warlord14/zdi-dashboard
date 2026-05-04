# ZDI-15-052: (0Day) Microsoft Word Line Formatting Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-052
- **ZDI-CAN:** ZDI-CAN-2485
- **Date:** 2015-02-27
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Alisa Esage
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-052/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the line formatting functionality. By providing a malformed .docx file, an attacker can cause a denial of service condition for the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/04/2014 - Report sent to vendor 08/04/2014 - ZDI received reply and case # from the vendor 01/13/2015 - ZDI requested any available update or ETA - no reply 01/21/2015 - ZDI notified of possible 0-day - no reply 02/09/2015 - ZDI notified the vendor that the case will-move to 0-day and is no longer eligible for extension 02/27/2015 - ZDI publishes advisory. 03/02/2015 - After multiple mails with no reply from this vendor prior to this 0-day posting, the ZDI did receive a post 0-day response from this vendor. The vendor notified that the case was closed previously and acknowledged that they failed to notify the ZDI at that time. Advisory updated based on feedback from vendor. -- Vendor Mitigation: The vendor did not provide any mitigations. -- Mitigation: Given the stated purpose of Microsoft Word, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2014-08-04 - Vulnerability reported to vendor
- 2015-02-27 - Coordinated public release of advisory
