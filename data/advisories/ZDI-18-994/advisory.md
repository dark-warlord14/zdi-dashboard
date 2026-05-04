# ZDI-18-994: (0Day) Wecon LeviStudioU hmi_bmplib_dll MulStatus szFilename Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-994
- **ZDI-CAN:** ZDI-CAN-6064
- **Date:** 2018-09-05
- **CVE:** CVE-2018-10602
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-994/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the G_Picture.xml file. When parsing the szFilename attribute of the MulStatus element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-212-03 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/11/2018 - ZDI disclosed the report to iCS-CERT 04/17/2018 - ICS-CERT acknowledged and added to ICS-VU-841553 08/09/2018 - ZDI sent a status request to the vendor 08/14/2018 - ICS-CERT replied that they did not have any update from the vendor 08/16/2018 - ZDI replied that we would notify them of the date of 0-day 08/31/2018 - ZDI notified ICS-CERT that the reports will 0-day 09/05/2018 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-04-11 - Vulnerability reported to vendor
- 2018-09-05 - Coordinated public release of advisory
- 2018-09-05 - Advisory Updated
