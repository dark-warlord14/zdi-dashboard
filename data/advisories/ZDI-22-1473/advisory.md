# ZDI-22-1473: (0Day) Corel CorelDRAW Graphics Suite PDF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1473
- **ZDI-CAN:** ZDI-CAN-16370
- **Date:** 2022-10-25
- **CVE:** CVE-2022-43615
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Corel
- **Affected Products:** CorelDRAW Graphics Suite
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1473/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Corel CorelDRAW Graphics Suite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Corel has issued an update to correct this vulnerability. More details can be found at: https://www.coreldraw.com/en/support/updates/cdgs2022/update.html

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-10-25 - Coordinated public release of advisory
- 2023-05-24 - Advisory Updated
