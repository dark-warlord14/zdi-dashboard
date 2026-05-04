# ZDI-21-1541: Apache Log4j StrSubstitutor Uncontrolled Recursion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1541
- **ZDI-CAN:** ZDI-CAN-16160
- **Date:** 2021-12-19
- **CVE:** CVE-2021-45105
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Apache
- **Affected Products:** Log4j
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1541/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Apache Log4j. Authentication is not required to exploit this vulnerability. The specific flaw exists within the StrSubstitutor class. The issue results from the lack of proper validation of user-supplied data, which can result in a resource exhaustion condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the process.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://logging.apache.org/log4j/2.x/security.html

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2021-12-19 - Coordinated public release of advisory
