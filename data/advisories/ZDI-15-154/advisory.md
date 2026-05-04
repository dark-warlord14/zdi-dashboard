# ZDI-15-154: HP TippingPoint SMS and vSMS JBoss RMI Remote Code Execution Vulnerabilty

## Metadata

- **ZDI ID:** ZDI-15-154
- **ZDI-CAN:** ZDI-CAN-2679
- **Date:** 2015-04-22
- **CVE:** CVE-2015-2117
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Security Management System
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-154/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP TippingPoint SMS and vSMS. Authentication is not required to exploit this vulnerability. The flaw exists within the Remote Method Invocation (RMI) component which is exposed on TCP ports 4444. Requests to these services are not authenticated and can be used to instantiate arbitrary classes or to upload and execute arbitrary archives. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SMS user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04626974

## Disclosure Timeline

- 2014-12-22 - Vulnerability reported to vendor
- 2015-04-22 - Coordinated public release of advisory
