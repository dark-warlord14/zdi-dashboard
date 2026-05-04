# ZDI-18-1001: (0Day) Hewlett Packard Enterprise Intelligent Management Center dbman decryptMsgAes Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1001
- **ZDI-CAN:** ZDI-CAN-6108
- **Date:** 2018-09-07
- **CVE:** CVE-2018-7114
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the decryption of encrypted messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=hpesbhf03906en_us This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/19/18 - ZDI reported vulnerability to vendor 04/19/18 - Vendor acknowledged and provided ZDI with ticket number 06/06/18 - Vendor replied indicating vendor did not consider the issue as a vulnerability 06/11/18 - ZDI replied expressing the disagreement and provided reasons and code to prove the argument 06/12/18 - Vendor acknowledged new details and confirmed details being forwarded to engineering 08/31/18 - ZDI contacted the vendor requesting an update 09/03/18 - ZDI notified the vendor that this case will 0-day on Friday September 7 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-04-19 - Vulnerability reported to vendor
- 2018-09-07 - Coordinated public release of advisory
- 2018-11-30 - Advisory Updated
