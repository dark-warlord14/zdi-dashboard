# ZDI-17-815: (0Day) Eaton ELCSoft EPC File Parsing Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-815
- **ZDI-CAN:** ZDI-CAN-4554
- **Date:** 2017-09-26
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Eaton
- **Affected Products:** ELCSoft
- **Credit:** axt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-815/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Eaton ELCSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of an EPC file. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/23/2017 and 03/28/2017 - ZDI disclosed the reports to ICS-CERT 03/24/2017 - ICS-CERT provided ZDI with an ICS-VU#, ICS-VU-380351 03/28/2017 - ICS-CERT acknowledged all 7 reports from ZDI for this vendor 08/11/2017 - ZDI sent a status inquiry to ICS-CERT 08/11/2017 - ICS-CERT replied that the vendor is working with a 3rd party component and had no ETA 08/30/2017 - ZDI asks ICS-CERT to notify the vendor that these will 0-day on 9/26 09/15/2017 - ZDI reminded ICS-CERT that these will 0-day on 9/26 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2017-03-28 - Vulnerability reported to vendor
- 2017-09-26 - Coordinated public release of advisory
