# ZDI-21-1208: (0Day) Fuji Electric Alpha5 Servo Operator C5P File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1208
- **ZDI-CAN:** ZDI-CAN-13939
- **Date:** 2021-10-15
- **CVE:** CVE-2022-21214
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha5
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1208/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Alpha5. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of C5P files in the Server Operator module. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/02/21 – ZDI reported the vulnerability to the vendor 09/02/21 – ICS-CERT indicated the vendor has been notified and requested an extension 09/03/21 – ZDI agreed to give them an extension 10/04/21 – ZDI requested an update 10/04/21 – ICS-CERT indicated that the vendor would have the fix ready by 12/31/21 10/05/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 10/14/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-06-02 - Vulnerability reported to vendor
- 2021-10-15 - Coordinated public release of advisory
- 2022-03-23 - Advisory Updated
