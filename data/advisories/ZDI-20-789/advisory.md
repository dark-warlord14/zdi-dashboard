# ZDI-20-789: (0Day) Delta Industrial Automation DOPSoft DPA File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-789
- **ZDI-CAN:** ZDI-CAN-10571
- **Date:** 2020-07-01
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-789/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPA files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/28/2020 – ZDI reported the vulnerabilities to ICS-CERT 03/06/2020 – ICS-CERT provided ZDI with an ICS-VU # 03/10/2020 – ICS-CERT communicated the vendor was targeting 06/30/2020 for the fix 06/08/2020 – ICS-CERT indicated the vendor requested an extension to 09/30/2020 06/08/2020 – ZDI replied that the extension was longer than ZDI could accommodate 06/11/2020 – ZDI notified ICS-CERT of the intention to publish these reports as 0-day advisories on 06/30/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-02-28 - Vulnerability reported to vendor
- 2020-07-01 - Coordinated public release of advisory
