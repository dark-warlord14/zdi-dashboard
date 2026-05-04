# ZDI-11-279: (0Day) Witness Systems eQuality Unify Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-279
- **ZDI-CAN:** ZDI-CAN-1097
- **Date:** 2011-09-02
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Witness Systems
- **Affected Products:** eQuality
- **Credit:** AbdulAziz Hariri of ThirdEyeTesters
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-279/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Witness Systems eQuality Suite. This application is bundled with Nortel Contact Recording and Quality Monitoring Suite. Authentication is not required to exploit this vulnerability. The flaw exists within the Unify2.exe component which listens by default on TCP port 6821. When handling a packet type the process trusts a remaining packet length value provided by the user and blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Due to the small number of installations using this software the risk of potential exploitation has been determined to be very low and therefore this issue will not be addressed. Avaya recommends implementing firewall rules that restrict access to trusted hosts to mitigate the risk. Witness Systems: No response was ever given.

## Disclosure Timeline

- 2011-03-01 - Vulnerability reported to vendor
- 2011-09-02 - Coordinated public release of advisory
