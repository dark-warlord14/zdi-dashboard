# ZDI-11-293: Avaya Identity Engines Ignition Server Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-293
- **ZDI-CAN:** ZDI-CAN-1095
- **Date:** 2011-10-18
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Avaya
- **Affected Products:** Identity Engines Ignition Server
- **Credit:** AbdulAziz Hariri of ThirdEyeTesters
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-293/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Nortel/Avaya Identity Engines Ignition Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AdminAccountManager process, which listens for GIOP requests over TCP ports 23456 and 23457 (SSL). The AdminAccountManager responds to remote requests for administrative functions without authentication. It is possible for a remote attacker to invoke the setAccountPassword operation for the default administrator account, effectively usurping administrator access. From there, it is trivial to execute arbitrary code remotely.

## Additional Details

Avaya has issued an update to correct this vulnerability. More details can be found at: http://support.avaya.com/css/Products/P0622/Security%20Advisories

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-10-18 - Coordinated public release of advisory
