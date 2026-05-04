# ZDI-16-354: (0Day) ActivePDF Toolkit ImageToPDF IAT Overwrite Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-354
- **ZDI-CAN:** ZDI-CAN-3123
- **Date:** 2016-05-24
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** ActivePDF
- **Affected Products:** Toolkit
- **Credit:** Context Information Security (Australia)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-354/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ActivePDF Toolkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ImageToPDF function. A specially crafted WPG file can overwrite IAT values. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/04/2015 - ZDI sent this vulnerability report to the vendor 11/04/2015 - The vendor replied with clarifying questions about the report 11/10/2015 - ZDI replied with clarification and further evidentiary files 11/12/2015 - The vendor replied with further clarifying questions 11/12/2015 - ZDI explained the nature of the report 02/29/2016 - ZDI requested an update 02/29/2016 - The vendor replied that "there is not currently a fix available, but they have identified a specific problem and are currently working on a resolution for that issue." 02/29/2016 - The ZDI replied that "the case has an expected date of 3/3, but is eligible for an extension to 5/4." and "Please note that after that the case will be disclosed publicly, as a 0-day." 04/27/2016 - The ZDI requested any available update 04/28/2016 - The vendor replied that "the issue is approved for Engineering resources but has not yet been assigned to a release." 05/04/2016 - ZDI notified the vendor that "this case will move to 0-day/public disclosure the week of 5/23." 05/04/2016 - ZDI received acknowledgement from the vendor that they "updated the Bug to reflect the new deadline for development." -- Mitigation: Given the stated purpose of ActivePDF Toolkit ImageToPDF, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2015-11-04 - Vulnerability reported to vendor
- 2016-05-24 - Coordinated public release of advisory
