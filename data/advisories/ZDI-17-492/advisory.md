# ZDI-17-492: AlienVault Unified Security Management nfcapd Process_ipfix_template_withdraw Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-492
- **ZDI-CAN:** ZDI-CAN-4416
- **Date:** 2017-07-20
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** 62600BCA031B9EB5CB4A74ADDDD6771E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-492/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault Unified Security Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within nfcapd's Process_ipfix_template_withdraw function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/8325/

## Disclosure Timeline

- 2017-01-10 - Vulnerability reported to vendor
- 2017-07-20 - Coordinated public release of advisory
- 2018-02-09 - Advisory Updated
