# ZDI-18-990: (0Day) Wecon LeviStudioU screendata Key ASCIIKey Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-990
- **ZDI-CAN:** ZDI-CAN-6055
- **Date:** 2018-09-05
- **CVE:** CVE-2018-10606
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-990/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of UMP files. When parsing the ASCIIKey attribute of the Key element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-212-03 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/05/2018 - ZDI disclosed the report to ICS-CERT 04/06/2018 - ICS-CERT acknowledged and added to ICS-VU-841553 08/09/2018 - ZDI sent a status request to the vendor 08/14/2018 - ICS-CERT replied that they did not have any update from the vendor 08/16/2018 - ZDI replied that we would notify them of the date of 0-day 08/31/2018 - ZDI notified ICS-CERT that the reports will 0-day 09/05/2018 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-04-05 - Vulnerability reported to vendor
- 2018-09-05 - Coordinated public release of advisory
- 2018-09-05 - Advisory Updated
