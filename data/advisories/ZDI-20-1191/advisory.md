# ZDI-20-1191: (0Day) Fuji Electric Tellus Lite V-Simulator 5 V8 File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1191
- **ZDI-CAN:** ZDI-CAN-10928
- **Date:** 2020-09-17
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Tellus Lite
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Tellus Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of V8 files by the V-Simulator 5 application. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/29/20 – ZDI reported the vulnerability to the ICS-CERT 08/03/20 – ZDI requested an update 08/03/20 – ICS-CERT indicated that the vendor was having problems validating the issue 08/18/20 – ZDI requested an update 08/18/20 – ICS-CERT indicated that they were working with the vendor on the case 09/08/20 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 09/17/20 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-04-29 - Vulnerability reported to vendor
- 2020-09-17 - Coordinated public release of advisory
