# ZDI-15-551: IBM System Networking Switch Center Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-551
- **ZDI-CAN:** ZDI-CAN-3008
- **Date:** 2015-11-10
- **CVE:** CVE-2015-7818
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** System Networking Switch Center
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-551/
## Vulnerability Details

This vulnerability allows local unprivileged attackers to execute arbitrary code on vulnerable installations of IBM System Networking Switch Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IBM SNSC Web Service, which listens by default on ports 40080 (HTTP) or 40443 (HTTPS) for requests to the administration panel. Because this service offers access to the Apache Axis AdminService, an unprivileged local attacker can publish arbitrary classes with the deployment method. An attacker can leverage this access to install arbitrary .jsp files on the server, which will by default run under the context of SYSTEM.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://support.lenovo.com/us/en/product_security/len_2015_074

## Disclosure Timeline

- 2015-06-23 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
