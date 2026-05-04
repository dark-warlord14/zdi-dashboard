# ZDI-11-017: Oracle Audit Vault av.action Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-017
- **ZDI-CAN:** ZDI-CAN-962
- **Date:** 2011-01-18
- **CVE:** CVE-2010-4449
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Audit Vault
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Audit Vault. Authentication is not required to exploit this vulnerability. The flaw exists within the av component which listens by default on TCP port 5700. When handling an action.execute request the process evaluates code provided as a parameter without proper validation. This allows for creation of arbitrary objects. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the oracle user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html

## Disclosure Timeline

- 2010-09-29 - Vulnerability reported to vendor
- 2011-01-18 - Coordinated public release of advisory
