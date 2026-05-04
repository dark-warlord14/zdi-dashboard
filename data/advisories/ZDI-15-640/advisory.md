# ZDI-15-640: Foxit FoxitCloudUpdateService Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-640
- **ZDI-CAN:** ZDI-CAN-3286
- **Date:** 2015-12-15
- **CVE:** CVE-2015-8843
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit Reader
- **Credit:** AbdulAziz Hariri of HP Zero Day Initiative and Jasiel Spelman of HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-640/
## Vulnerability Details

This vulnerability allows local attackers to elevate privileges on vulnerable installations of Foxit Reader. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FoxitCloudUpdateService service. An attacker can trigger a memory corruption condition by writing certain data to a shared memory region. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2015-09-14 - Vulnerability reported to vendor
- 2015-12-15 - Coordinated public release of advisory
