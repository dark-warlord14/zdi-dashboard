# ZDI-17-700: (0Day) Delta Industrial Automation WPLSoft dvp File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-700
- **ZDI-CAN:** ZDI-CAN-4428
- **Date:** 2017-08-24
- **CVE:** CVE-2018-7509
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** WPLSoft
- **Credit:** axt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-700/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation WPLSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of .dvp files. Crafted data in a .dvp file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-058-02 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/01/17 - ZDI disclosed reports to ICS-CERT 02/07/17 - ICS-CERT provided ZDI with an ICS-VU # ICS-VU-974568 03/16/17 - ICS-CERT asked ZDI questions about reproduction 03/27/17 - ICS-CERT asked ZDI again some questions about reproduction 06/07/17 - ICS-CERT offered ZDI a pre-release patch to test 06/07/17 - ZDI replied that we cannot do the testing for the vendor 07/20/17 - ZDI sent a mail to ICS-CERT asking the status 07/26/17 - ICS-CERT advised that the vendor has a new version they believe addressed the reports (though to ZDI knowledge, no advisory was released) 08/02/17 - ZDI advised ICS-CERT that our finder indicated that the vulnerabilities are still present 08/11/17 - ZDI wrote ICS-CERT to indicate the intention to move these reports to 0-day on 8/24 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-08-24 - Coordinated public release of advisory
- 2018-03-28 - Advisory Updated
