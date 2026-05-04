# ZDI-18-829: (0Day) Wecon LeviStudioU aetlog Alarm WordAddr9 Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-829
- **ZDI-CAN:** ZDI-CAN-5910
- **Date:** 2018-07-26
- **CVE:** CVE-2018-10602
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-829/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of UMP files. When parsing the Alarm WordAddr9 element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-212-03 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/07/18 - ZDI disclosed the report to ICS-CERT 03/12/18 - ICS-CERT assigned ICS‑VU‑031741 and notified ZDI 07/06/18 - ZDI inquired the status of ICS‑VU‑031741 07/09/18 - ICS-CERT replied that they would advise the vendor 07/19/18 - ZDI advised ICS-CERT of the intended 0-day date: 07/26/2018 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-03-23 - Vulnerability reported to vendor
- 2018-07-26 - Coordinated public release of advisory
- 2018-08-02 - Advisory Updated
