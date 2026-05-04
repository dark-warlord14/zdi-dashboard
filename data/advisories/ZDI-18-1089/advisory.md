# ZDI-18-1089: (0Day) Wecon LeviStudioU cximageu TIFF Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1089
- **ZDI-CAN:** ZDI-CAN-6242
- **Date:** 2018-09-26
- **CVE:** CVE-2018-10606
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Mat Powell - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1089/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIFF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the Administrator.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-212-03 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/18/18 - ZDI disclosed the reports to ICS-CERT 07/06/18 - ZDI inquired about the status of the reports 09/19/18 - ZDI notified ICS-CERT of the intent to 0-day these on 9/26 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-09-26 - Coordinated public release of advisory
- 2018-09-26 - Advisory Updated
