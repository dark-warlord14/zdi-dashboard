# ZDI-15-409: (0Day) ASUS TM-AC1900 httpd Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-409
- **ZDI-CAN:** ZDI-CAN-3035
- **Date:** 2015-09-02
- **CVE:** CVE-2015-6949
- **CVSS:** 7.9
- **CVSS Vector:** AV:A/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ASUS
- **Affected Products:** TM-AC1900
- **Credit:** Elvis Collado - HP DVLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-409/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the ASUS TM-1900. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP header parsing routine. The issue lies in the failure to check the size of header values. An attacker could leverage this vulnerability to execute code within the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 07/09/2015 - ZDI emailed ASUS requested contact 07/28/2015 - ZDI emailed ASUS requested contact 08/13/2015 - ZDI emailed ASUS requested contact 08/21/2015 - ZDI emailed ASUS requested contact -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2015-05-05 - Vulnerability reported to vendor
- 2015-09-02 - Coordinated public release of advisory
