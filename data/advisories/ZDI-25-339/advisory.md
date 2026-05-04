# ZDI-25-339: JupyterLab Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-339
- **ZDI-CAN:** ZDI-CAN-25932
- **Date:** 2025-06-10
- **CVE:** CVE-2025-30167
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Jupyter
- **Affected Products:** JupyterLab
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-339/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of JupyterLab. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Additionally, the vulnerability is triggered only when a target user makes use of the product. The specific flaw exists within the jupyter-lab process. The process loads a configuration script from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

Jupyter has issued an update to correct this vulnerability. More details can be found at: https://github.com/jupyter/jupyter_core/security/advisories/GHSA-33p9-3p43-82vq

## Disclosure Timeline

- 2025-02-13 - Vulnerability reported to vendor
- 2025-06-10 - Coordinated public release of advisory
- 2025-06-10 - Advisory Updated
